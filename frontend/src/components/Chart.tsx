"use client";

import React, { useState } from "react";

import {
  ScatterChart,
  Scatter,
  XAxis,
  YAxis,
  Legend,
  ReferenceLine,
  LegendPayload,
} from "recharts";

import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart";

const COLORS = [
  "#1f77b4",
  "#ff7f0e",
  "#2ca02c",
  "#d62728",
  "#9467bd",
  "#8c564b",
  "#e377c2",
  "#7f7f7f",
  "#bcbd22",
  "#17becf",
];

const axisConfig = {
  fontSize: 12,
  stroke: "#c9a0ff",
  strokeWidth: 0.5,
};

const chartConfig = {
  x: {
    label: "Episode",
  },
  y: {
    label: "Rating",
  },
} satisfies ChartConfig;

export default function ChartComponent({ seriesData }) {
  if (!seriesData || !seriesData.episodes) {
    return <p className="text-center text-red-500">No episode data found.</p>;
  }

  let finalEpisodes: number[] = [];
  let currentEpisode: number = seriesData.episodes[0].episodenumber - 1;

  const groupedRatingsData = seriesData.episodes.reduce((acc, ep, index) => {
    if (!acc[ep.seasonnumber]) {
      acc[ep.seasonnumber] = [];
      finalEpisodes.push(currentEpisode);
    }

    acc[ep.seasonnumber].push({
      x: currentEpisode + 1,
      y: ep.averagerating,
      rating: ep.averagerating,
      numvotes: ep.numvotes,
      season: ep.seasonnumber,
      episode: ep.episodenumber,
      primarytitle: ep.primarytitle,
      tconst: ep.tconst,
      color: COLORS[(ep.seasonnumber - 1) % COLORS.length],
    });

    currentEpisode = currentEpisode + 1;

    return acc;
  }, {});

  finalEpisodes.push(currentEpisode);

  const uniqueSeasons = Object.keys(groupedRatingsData).map(Number);
  const labelSeasons: Record<string, boolean | null> = uniqueSeasons.reduce(
    (acc, season) => {
      acc[`Season ${season}`] = false;
      return acc;
    },
    {} as Record<string, boolean>
  );

  labelSeasons["hover"] = null;

  const [barProps, setBarProps] = useState(labelSeasons);

  const handleLegendMouseEnter = (e: LegendPayload) => {
    console.log("Ads", e);
    if (!barProps[e.value]) {
      setBarProps({ ...barProps, hover: e.value });
    }
  };

  const handleLegendMouseLeave = (e: LegendPayload) => {
    setBarProps({ ...barProps, hover: null });
  };

  const selectSeasonLegend = (e: LegendPayload) => {
    setBarProps({
      ...barProps,
      [e.value]: !barProps[e.value],
      hover: null,
    });
  };

  return (
    <div>
      <ChartContainer config={chartConfig} className="w-full h-96">
        <ScatterChart
          margin={{ top: 20, right: 30, left: 20, bottom: 40 }}
          data={groupedRatingsData}
        >
          <XAxis
            type="number"
            dataKey="x"
            name="xaxis"
            label={{
              value: "Episode",
              position: "insideBottom",
              ...axisConfig,
            }}
            ticks={finalEpisodes.slice(1)}
            tickLine={false}
            tick={axisConfig}
            domain={[0, finalEpisodes[finalEpisodes.length - 1]+0.5]}
          />

          <YAxis
            type="number"
            dataKey="y"
            domain={[0, 10]}
            ticks={[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
            label={{
              value: "Episode Rating",
              angle: -90,
              position: "Left",
              ...axisConfig,
            }}
            tick={axisConfig}
          />

          <ChartTooltip
            content={
              <ChartTooltipContent
                indicator="dot"
                className="w-[180px]"
                labelFormatter={(value, name) => (
                  <strong>
                    {name[0].payload.season}.{name[0].payload.episode} -{" "}
                    {name[0].payload.primarytitle}
                  </strong>
                )}
                formatter={(value, name, item, index) => {
                  if (name === "xaxis") {
                    return null;
                  }

                  return (
                    <>
                      <div
                        className="h-2.5 w-2.5 shrink-0 rounded-[2px] bg-[--color-bg]"
                        style={
                          {
                            "--color-bg": item.payload.color,
                          } as React.CSSProperties
                        }
                      />
                      <div>{value.toFixed(1)}</div>
                      <div className="ml-auto flex items-baseline gap-0.5 font-mono font-medium tabular-nums text-foreground">
                        <span className="font-normal text-muted-foreground">
                          ({item.payload.numvotes} votes)
                        </span>
                      </div>
                      {/* {index === 1 && (
                        <a
                          href={`https://www.imdb.com/title/${item.payload.tconst}/`}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-blue-500 underline hover:text-blue-700"
                        >
                          Go to IMDb
                        </a>
                      )} */}
                    </>
                  );
                }}
              />
            }
            cursor={false}
            defaultIndex={1}
          />

          <Legend
            wrapperStyle={{
              position: "relative",
            }}
            onClick={selectSeasonLegend}
            onMouseOver={handleLegendMouseEnter}
            onMouseOut={handleLegendMouseLeave}
          />

          {uniqueSeasons.map((season, idx) => {
            return (
              <Scatter
                key={`season-${season}`}
                name={`Season ${season}`}
                data={groupedRatingsData[season]}
                fill={COLORS[(season - 1) % COLORS.length]}
                hide={barProps[`Season ${season}`] === true}
                fillOpacity={Number(
                  barProps.hover === `Season ${season}` || !barProps.hover
                    ? 1
                    : 0.25
                )}
              >
                {/* {groupedRatingsData[season].map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))} */}
              </Scatter>
            );
          })}
          {finalEpisodes.slice(1).map((value, index) => (
            <ReferenceLine
              key={`XRefLine-${index}`}
              x={value + 0.5}
              stroke="black"
              strokeDasharray="5 2"
              strokeWidth={0.3}
            />
          ))}
          {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((value, index) => (
            <ReferenceLine
              key={`YRefLine-${index}`}
              y={value}
              stroke="#4b0082"
              strokeDasharray="5 1"
              strokeWidth={0.2}
            />
          ))}
        </ScatterChart>
      </ChartContainer>
    </div>
  );
}
