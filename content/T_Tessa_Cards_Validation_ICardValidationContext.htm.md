# ICardValidationContext - интерфейс
Контекст валидации карточки, содержащий проверяемые данные карточки и методы
получения объектов, которые выполняют построение результата валидации для
различных элементов проверяемой карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardValidationContext : ISealable
VB __Копировать
     Public Interface ICardValidationContext
    	Inherits ISealable
C++ __Копировать
     public interface class ICardValidationContext : ISealable
F# __Копировать
     type ICardValidationContext = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[CancellationToken](P_Tessa_Cards_Validation_ICardValidationContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardMetadata](P_Tessa_Cards_Validation_ICardValidationContext_CardMetadata.htm)|
Метаинформация по типам карточек, используемая в процессе валидации.  
[ExternalContextInfo](P_Tessa_Cards_Validation_ICardValidationContext_ExternalContextInfo.htm)|
Произвольно структурированная информация из внешнего контекста (например,
контекста сохранения карточки), которая может быть заполнена валидатором и
использована либо другими валидаторами, либо внешними расширениями. Когда
внешний контекст неизвестен, будет создан пустой объект, но при этом свойство
никогда не возвращает null.  
[ForceWarnings](P_Tessa_Cards_Validation_ICardValidationContext_ForceWarnings.htm)|
Признак того, что валидаторы-предупреждения срабатывают даже в том случае,
если они не должны срабатывать, например, на клиенте. Это полезно, если
выполняется валидация на клиенте без валидации на сервере.  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Limitations](P_Tessa_Cards_Validation_ICardValidationContext_Limitations.htm)|
Объект, ограничивающий доступность объектов для валидации.  
[MainCard](P_Tessa_Cards_Validation_ICardValidationContext_MainCard.htm)|
Основная карточка, для которой выполняется валидация.  
[MainCardMetadataBinder](P_Tessa_Cards_Validation_ICardValidationContext_MainCardMetadataBinder.htm)|
Объект, выполняющий действия с основной карточкой, для которой выполняется
валидация.  
[MainCardType](P_Tessa_Cards_Validation_ICardValidationContext_MainCardType.htm)|
Тип основной карточки, для которой выполняется валидация.  
[Session](P_Tessa_Cards_Validation_ICardValidationContext_Session.htm)| Сессия
пользователя, в процессе работы которого выполняется валидация.  
[StoreMode](P_Tessa_Cards_Validation_ICardValidationContext_StoreMode.htm)|
Способ сохранения проверяемого объекта - карточки, файла или задания.  
[TaskCard](P_Tessa_Cards_Validation_ICardValidationContext_TaskCard.htm)|
Карточка задания, валидация которой выполняется, или null, если задание
завершается без данных карточки или валидация задания не выполняется.  
[TaskCardMetadataBinder](P_Tessa_Cards_Validation_ICardValidationContext_TaskCardMetadataBinder.htm)|
Объект, выполняющий действия с карточкой задания, для которой выполняется
валидация, или null, если задание завершается без данных карточки или
валидация задания не выполняется.  
[TaskCardType](P_Tessa_Cards_Validation_ICardValidationContext_TaskCardType.htm)|
Тип карточки задания, для которой выполняется валидация, или null, если
валидация задания не выполняется.  
[ValidationMode](P_Tessa_Cards_Validation_ICardValidationContext_ValidationMode.htm)|
Способ выполнения валидации.  
##  __Методы
[BuildResult](M_Tessa_Cards_Validation_ICardValidationContext_BuildResult.htm)|
Выполняет построение результата валидации карточки.  
---|---  
[GetCardValidator](M_Tessa_Cards_Validation_ICardValidationContext_GetCardValidator.htm)|
Возвращает объект, выполняющий построение результата валидации для всей
карточки.  
[GetEntryFieldValidator](M_Tessa_Cards_Validation_ICardValidationContext_GetEntryFieldValidator.htm)|
Возвращает объект, выполняющий построение результата валидации для заданного
поля строковой секции.  
[GetSectionValidator](M_Tessa_Cards_Validation_ICardValidationContext_GetSectionValidator.htm)|
Возвращает объект, выполняющий построение результата валидации для строковой,
коллекционной или древовидной секции карточки.  
[GetTableFieldValidator](M_Tessa_Cards_Validation_ICardValidationContext_GetTableFieldValidator.htm)|
Возвращает объект, выполняющий построение результата валидации для заданного
поля строки коллекционной или древовидной секции.  
[GetTableRowValidator](M_Tessa_Cards_Validation_ICardValidationContext_GetTableRowValidator.htm)|
Возвращает объект, выполняющий построение результата валидации для строки
коллекционной или древовидной секции.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
