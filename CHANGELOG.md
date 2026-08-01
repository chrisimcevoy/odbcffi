# Changelog

## [0.2.0](https://github.com/chrisimcevoy/odbcffi/compare/v0.1.0...v0.2.0) (2026-08-01)


### Features

* SQLCloseCursor ([#35](https://github.com/chrisimcevoy/odbcffi/issues/35)) ([e890ab6](https://github.com/chrisimcevoy/odbcffi/commit/e890ab6f4ea17e20f95178ae5e6bbff7700697dd))
* SQLDriversW ([#11](https://github.com/chrisimcevoy/odbcffi/issues/11)) ([7448b2c](https://github.com/chrisimcevoy/odbcffi/commit/7448b2cf94510ffc1a8a3e8f47959abf8ba2673e))
* SQLEndTran ([#37](https://github.com/chrisimcevoy/odbcffi/issues/37)) ([ac39a5f](https://github.com/chrisimcevoy/odbcffi/commit/ac39a5fb346d98df55a03163db4d5b506160ca17))
* SQLExecDirectW ([#34](https://github.com/chrisimcevoy/odbcffi/issues/34)) ([60e8cfc](https://github.com/chrisimcevoy/odbcffi/commit/60e8cfc54236d308291c7e6406cc9619c5fbfc32))
* SQLGetFunctions ([#103](https://github.com/chrisimcevoy/odbcffi/issues/103)) ([ab71aef](https://github.com/chrisimcevoy/odbcffi/commit/ab71aef4e1b75d80da327c2c6c9ea24678eb31d3))
* SQLGetTypeInfoW ([#28](https://github.com/chrisimcevoy/odbcffi/issues/28)) ([62a0834](https://github.com/chrisimcevoy/odbcffi/commit/62a08345407511e8b296cfb9cf719077e1d1349e))
* SQLNativeSQL ([#99](https://github.com/chrisimcevoy/odbcffi/issues/99)) ([aedd3ff](https://github.com/chrisimcevoy/odbcffi/commit/aedd3ffe63e9d11c9f214ff5d0c7e47b5b4518cc))
* SQLRowCount ([#36](https://github.com/chrisimcevoy/odbcffi/issues/36)) ([1abb9e4](https://github.com/chrisimcevoy/odbcffi/commit/1abb9e4ad5ce65cc4dd2106cd6a2bef5a7be4e91))


### Bug Fixes

* create an `FFI` object per `DriverManager` instance ([425f196](https://github.com/chrisimcevoy/odbcffi/commit/425f1966b68d2c4717ceb5a05fef900a9c95aad3))
* establish consistent retry pattern for string truncation ([#16](https://github.com/chrisimcevoy/odbcffi/issues/16)) ([30affe2](https://github.com/chrisimcevoy/odbcffi/commit/30affe2863e5f514f38a62bc031fab4dc54fe0f9))
* retry SQLGetInfoW when data is truncated ([#15](https://github.com/chrisimcevoy/odbcffi/issues/15)) ([0012e6f](https://github.com/chrisimcevoy/odbcffi/commit/0012e6fba395d52bfe0076ffe51a58ee9eaacc2a))


### Reverts

* "ci: run `test` job steps in parallel ([#29](https://github.com/chrisimcevoy/odbcffi/issues/29))" ([#30](https://github.com/chrisimcevoy/odbcffi/issues/30)) ([3a1694c](https://github.com/chrisimcevoy/odbcffi/commit/3a1694c2829e81344e265700ed007d202d78bbcf))

## 0.1.0 (2026-05-16)


### Features

* SQLGetInfoW ([#3](https://github.com/chrisimcevoy/odbcffi/issues/3)) ([1aca0ac](https://github.com/chrisimcevoy/odbcffi/commit/1aca0ac6f97876a5a8fff08e7451c29b3985c554))
