# IMergeTree<TMergeObject, TMergeOptions> \- интерфейс
Представляет дерево слияния
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMergeTree<TMergeObject, TMergeOptions>
    where TMergeOptions : IMergeOptions
VB __Копировать
     Public Interface IMergeTree(Of TMergeObject, TMergeOptions As IMergeOptions)
C++ __Копировать
    generic<typename TMergeObject, typename TMergeOptions>
    where TMergeOptions : IMergeOptions
    public interface class IMergeTree
F# __Копировать
     type IMergeTree<'TMergeObject, 'TMergeOptions when 'TMergeOptions : IMergeOptions> = interface end
#### Параметры типа
TMergeObject
    Тип, представляющий объекты слияния
TMergeOptions
    Тип опций слияния
##  __Свойства
[Tiers](P_Tessa_SmartMerge_IMergeTree_2_Tiers.htm)|  Уровень дерева слияния  
---|---  
## __Методы
[Merge](M_Tessa_SmartMerge_IMergeTree_2_Merge.htm)|  Производит слияние с
другим деревом  
---|---  
## __См. также
#### Ссылки
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
