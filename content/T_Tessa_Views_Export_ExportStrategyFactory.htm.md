# ExportStrategyFactory - делегат
Делегат фабрики создания стратегии экспорта данных
## __Definition
 **Пространство имён:** [Tessa.Views.Export](N_Tessa_Views_Export.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    public delegate IExportGeneratorStrategy ExportStrategyFactory(
    	Guid exportType
    )
VB __Копировать
    <CanBeNullAttribute>
    Public Delegate Function ExportStrategyFactory ( 
    	exportType As Guid
    ) As IExportGeneratorStrategy
C++ __Копировать
    [CanBeNullAttribute]
    public delegate IExportGeneratorStrategy^ ExportStrategyFactory(
    	Guid exportType
    )
F# __Копировать
     [<CanBeNullAttribute>]
    type ExportStrategyFactory = 
        delegate of 
            exportType : Guid -> IExportGeneratorStrategy
#### Параметры
exportType [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Вид стратегии экспорта
#### Возвращаемое значение
[IExportGeneratorStrategy](T_Tessa_Views_Export_IExportGeneratorStrategy.htm)  
Стратегия экспорта данных или null, если тип экспорта не поддерживается
##  __См. также
#### Ссылки
[Tessa.Views.Export - пространство имён](N_Tessa_Views_Export.htm)
