# Changelog

## [0.2.0](https://github.com/chrisimcevoy/odbcffi/compare/v0.1.0...v0.2.0) (2026-06-06)


### Features

* SQLDriversW ([#11](https://github.com/chrisimcevoy/odbcffi/issues/11)) ([7448b2c](https://github.com/chrisimcevoy/odbcffi/commit/7448b2cf94510ffc1a8a3e8f47959abf8ba2673e))


### Bug Fixes

* create an `FFI` object per `DriverManager` instance ([425f196](https://github.com/chrisimcevoy/odbcffi/commit/425f1966b68d2c4717ceb5a05fef900a9c95aad3))
* establish consistent retry pattern for string truncation ([#16](https://github.com/chrisimcevoy/odbcffi/issues/16)) ([30affe2](https://github.com/chrisimcevoy/odbcffi/commit/30affe2863e5f514f38a62bc031fab4dc54fe0f9))
* retry SQLGetInfoW when data is truncated ([#15](https://github.com/chrisimcevoy/odbcffi/issues/15)) ([0012e6f](https://github.com/chrisimcevoy/odbcffi/commit/0012e6fba395d52bfe0076ffe51a58ee9eaacc2a))

## 0.1.0 (2026-05-16)


### Features

* SQLGetInfoW ([#3](https://github.com/chrisimcevoy/odbcffi/issues/3)) ([1aca0ac](https://github.com/chrisimcevoy/odbcffi/commit/1aca0ac6f97876a5a8fff08e7451c29b3985c554))
