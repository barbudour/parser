# IMergeResult<TMergeObject> \- интерфейс
Представляет обзект содержащий в себе результаты слияния и имеет возможность
применить их к объекту с которым происходит слияние.
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMergeResult<TMergeObject>
VB __Копировать
     Public Interface IMergeResult(Of TMergeObject)
C++ __Копировать
    generic<typename TMergeObject>
    public interface class IMergeResult
F# __Копировать
     type IMergeResult<'TMergeObject> = interface end
#### Параметры типа
TMergeObject
    Тип объектов для которых производится слияние
##  __Свойства
[MergeResultItems](P_Tessa_SmartMerge_IMergeResult_1_MergeResultItems.htm)|
Список результатов слияния.  
---|---  
[ValidationResult](P_Tessa_SmartMerge_IMergeResult_1_ValidationResult.htm)|
Результат валидации.  
## __Методы
[ApplyAsync](M_Tessa_SmartMerge_IMergeResult_1_ApplyAsync.htm)|  Применяет
результат слияния к объекту слияния.  
---|---  
## __См. также
#### Ссылки
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
