# IMergeContext<TMergeOptions> \- интерфейс
Представляет объект контекста для логики слияния, содержащий необходимую для
этого слияния информацию
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMergeContext<out TMergeOptions>
    where TMergeOptions : IMergeOptions
VB __Копировать
     Public Interface IMergeContext(Of Out TMergeOptions As IMergeOptions)
C++ __Копировать
    generic<typename TMergeOptions>
    where TMergeOptions : IMergeOptions
    public interface class IMergeContext
F# __Копировать
     type IMergeContext<'TMergeOptions when 'TMergeOptions : IMergeOptions> = interface end
#### Параметры типа
TMergeOptions
    Тип опций слияния
##  __Свойства
[ComparisonLevels](P_Tessa_SmartMerge_IMergeContext_1_ComparisonLevels.htm)|
Количество уровней сравнения при сравнении узлов  
---|---  
[Logger](P_Tessa_SmartMerge_IMergeContext_1_Logger.htm)|  Кастомный логгер  
[MergeObject](P_Tessa_SmartMerge_IMergeContext_1_MergeObject.htm)|  Объект
слияния  
[MergeOptions](P_Tessa_SmartMerge_IMergeContext_1_MergeOptions.htm)|  Опции
слияния  
[ValidationResult](P_Tessa_SmartMerge_IMergeContext_1_ValidationResult.htm)|
Билдер результата валидации  
## __См. также
#### Ссылки
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
