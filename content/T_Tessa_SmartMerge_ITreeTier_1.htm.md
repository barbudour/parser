# ITreeTier<TMergeObject> \- интерфейс
Представляет уровень в дереве слияния
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITreeTier<TMergeObject>
VB __Копировать
     Public Interface ITreeTier(Of TMergeObject)
C++ __Копировать
    generic<typename TMergeObject>
    public interface class ITreeTier
F# __Копировать
     type ITreeTier<'TMergeObject> = interface end
#### Параметры типа
TMergeObject
    Тип объектов для которых производится слияние
##  __Свойства
[LookupsByLevel](P_Tessa_SmartMerge_ITreeTier_1_LookupsByLevel.htm)|  Список
лукапов по каждому уровню сравнения для текущего уровня дерева слияния (для
эффективного сравнения)  
---|---  
[Nodes](P_Tessa_SmartMerge_ITreeTier_1_Nodes.htm)|  Список узлов,
принедлежащих текущему уровню дерева слияния  
## __Методы
[FindByKey](M_Tessa_SmartMerge_ITreeTier_1_FindByKey.htm)|  Поиск ноды по
ключу, в зависимости от уровня сравнения  
---|---  
## __См. также
#### Ссылки
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
