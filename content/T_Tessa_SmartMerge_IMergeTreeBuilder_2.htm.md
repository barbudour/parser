# IMergeTreeBuilder<TMergeObject, TMergeOptions> \- интерфейс
Строит дерево слияния
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMergeTreeBuilder<TMergeObject, TMergeOptions>
    where TMergeOptions : IMergeOptions
VB __Копировать
     Public Interface IMergeTreeBuilder(Of TMergeObject, TMergeOptions As IMergeOptions)
C++ __Копировать
    generic<typename TMergeObject, typename TMergeOptions>
    where TMergeOptions : IMergeOptions
    public interface class IMergeTreeBuilder
F# __Копировать
     type IMergeTreeBuilder<'TMergeObject, 'TMergeOptions when 'TMergeOptions : IMergeOptions> = interface end
#### Параметры типа
TMergeObject
    Тип объектов для которых производится слияние
TMergeOptions
    Тип опций слияния
##  __Методы
[Build](M_Tessa_SmartMerge_IMergeTreeBuilder_2_Build.htm)|  Логика построения
дерева слияния  
---|---  
## __См. также
#### Ссылки
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
