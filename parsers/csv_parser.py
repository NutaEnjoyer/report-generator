class CSVParser:
    RATE_COLS = ["rate", "salary", "hourly_rate"]
    def _parse_csv_file(self, path: str) -> list[dict[str, str]]:
        all_rows: list[dict[str, str]] = []
        with open(path, "r", encoding="utf-8") as f:
            lines: list[str] = f.read().strip().split("\n")
            header: list[str] = [col.strip() for col in lines[0].split(",")]
            normalized_header: list[str] = self._normalize_header(header)

            for line in lines[1:]:
                values: list[str] = [val.strip() for val in line.split(",")]
                row = dict(zip(normalized_header, values))
                all_rows.append(row)

        return all_rows


    def parse_csv_files(self, paths: list[str]) -> list[dict]:
        all_rows: list[dict] = []
        for path in paths:
            all_rows.extend(self._parse_csv_file(path))

        return all_rows


    def _normalize_header(self, header: list[str]) -> list[str]:
        normalized_header: list[str] = []
        for col in header:
            col_lower: str = col.strip().lower()
            if col_lower in self.RATE_COLS:
                normalized_header.append("rate")
            else:
                normalized_header.append(col_lower)

        return normalized_header
