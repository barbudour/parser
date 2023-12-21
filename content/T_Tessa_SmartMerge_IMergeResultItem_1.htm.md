# IMergeResultItem<TMergeObject> \- интерфейс
Представляет результат слияния, а также логику применения этого результата к
объекту слияния
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMergeResultItem<in TMergeObject>
VB __Копировать
     Public Interface IMergeResultItem(Of In TMergeObject)
C++ __Копировать
    generic<typename TMergeObject>
    public interface class IMergeResultItem
F# __Копировать
     type IMergeResultItem<'TMergeObject> = interface end
#### Параметры типа
TMergeObject
    Тип объектов для которых производится слияние
##  __Методы
[ApplyAsync](M_Tessa_SmartMerge_IMergeResultItem_1_ApplyAsync.htm)|  Применяет
результат слияния к объекту.  
---|---  
## __См. также
#### Ссылки
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
