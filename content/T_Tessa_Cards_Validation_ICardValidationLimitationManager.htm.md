# ICardValidationLimitationManager - интерфейс
Объект, ограничивающий доступность объектов для валидации.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardValidationLimitationManager : ISealable
VB __Копировать
     Public Interface ICardValidationLimitationManager
    	Inherits ISealable
C++ __Копировать
     public interface class ICardValidationLimitationManager : ISealable
F# __Копировать
     type ICardValidationLimitationManager = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
---|---  
##  __Методы
[ClearLimitations](M_Tessa_Cards_Validation_ICardValidationLimitationManager_ClearLimitations.htm)|
Удаляет все добавленные ограничения.  
---|---  
[ColumnIsAllowed](M_Tessa_Cards_Validation_ICardValidationLimitationManager_ColumnIsAllowed.htm)|
Возвращает признак того, что колонка из указанной секции является доступной.  
[ExcludeColumns](M_Tessa_Cards_Validation_ICardValidationLimitationManager_ExcludeColumns.htm)|
Исключает набор колонок для указанной секции из доступных для валидатора. Если
колонка исключена из проверки, то валидаторы по ней не выполняются.  
[ExcludeSections](M_Tessa_Cards_Validation_ICardValidationLimitationManager_ExcludeSections.htm)|
Исключает набор секций из доступных для валидатора. Если секция исключена из
проверки, то валидаторы по ней не выполняются.  
[GetCardResult](M_Tessa_Cards_Validation_ICardValidationLimitationManager_GetCardResult.htm)|
Возвращает результат валидации для данных карточки, в котором ограничивается
набор сообщений для заданных секций и их строк.  
[LimitRows](M_Tessa_Cards_Validation_ICardValidationLimitationManager_LimitRows.htm)|
Ограничивает набор строк, доступных в секции. Добавление ограничений по
строкам секции также добавляет ограничение на эту секцию, если она не была
добавлена.  
[LimitSections](M_Tessa_Cards_Validation_ICardValidationLimitationManager_LimitSections.htm)|
Ограничивает набор секций, доступных для валидатора. Если ограничение секций
не выполнялось, то валидация выполняется по всем секциям, иначе только по
заданным. Указание коллекционной секции не означает автоматически возможность
редактировать любые строки этой секции.  
[RowIsAllowed](M_Tessa_Cards_Validation_ICardValidationLimitationManager_RowIsAllowed.htm)|
Возвращает признак того, что строка с заданным идентификатором в указанной
секции является доступной. При этом ограничений либо не должно быть вообще,
либо разрешено использование конкретно заданной строки в секции.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[SectionIsAllowed](M_Tessa_Cards_Validation_ICardValidationLimitationManager_SectionIsAllowed.htm)|
Возвращает признак того, что секция с заданным именем является доступной.  
##  __См. также
#### Ссылки
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
