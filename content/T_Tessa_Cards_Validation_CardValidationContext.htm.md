# CardValidationContext - класс
Контекст валидации карточки, содержащий проверяемые данные карточки и методы
получения объектов, которые выполняют построение результата валидации для
различных элементов проверяемой карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardValidationContext : ICardValidationContext, 
    	ISealable, IAsyncInitializable
VB __Копировать
     Public NotInheritable Class CardValidationContext
    	Implements ICardValidationContext, ISealable, IAsyncInitializable
C++ __Копировать
     public ref class CardValidationContext sealed : ICardValidationContext, 
    	ISealable, IAsyncInitializable
F# __Копировать
     [<SealedAttribute>]
    type CardValidationContext = 
        class
            interface ICardValidationContext
            interface ISealable
            interface IAsyncInitializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardValidationContext
Implements
    [ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm), [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[CardValidationContext(Card, CardType, CardStoreMode, ICardMetadata, ISession,
ISerializableObject, ICardValidationLimitationManager, CardValidationMode,
ICardMetadataBinder,
CancellationToken)](M_Tessa_Cards_Validation_CardValidationContext__ctor_1.htm)|
Создаёт экземпляр класса с указанием основной карточки, валидацию которых
требуется выполнить. После вызова конструктора используется асинхронную
инициализацию в методе
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).  
---|---  
[CardValidationContext(Card, CardType, CardStoreMode, Card, CardType,
ICardMetadata, ISession, ISerializableObject,
ICardValidationLimitationManager, CardValidationMode, ICardMetadataBinder,
ICardMetadataBinder,
CancellationToken)](M_Tessa_Cards_Validation_CardValidationContext__ctor.htm)|
Создаёт экземпляр класса с указанием основной карточки и её карточки задания,
валидацию которых требуется выполнить. После вызова конструктора используется
асинхронную инициализацию в методе
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).  
## __Свойства
[CancellationToken](P_Tessa_Cards_Validation_CardValidationContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardMetadata](P_Tessa_Cards_Validation_CardValidationContext_CardMetadata.htm)|
Метаинформация по типам карточек, используемая в процессе валидации.  
[ExternalContextInfo](P_Tessa_Cards_Validation_CardValidationContext_ExternalContextInfo.htm)|
Произвольно структурированная информация из внешнего контекста (например,
контекста сохранения карточки), которая может быть заполнена валидатором и
использована либо другими валидаторами, либо внешними расширениями. Когда
внешний контекст неизвестен, будет создан пустой объект, но при этом свойство
никогда не возвращает null.  
[ForceWarnings](P_Tessa_Cards_Validation_CardValidationContext_ForceWarnings.htm)|
Признак того, что валидаторы-предупреждения срабатывают даже в том случае,
если они не должны срабатывать, например, на клиенте. Это полезно, если
выполняется валидация на клиенте без валидации на сервере.  
[IsSealed](P_Tessa_Cards_Validation_CardValidationContext_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
[Limitations](P_Tessa_Cards_Validation_CardValidationContext_Limitations.htm)|
Объект, ограничивающий доступность объектов для валидации.  
[MainCard](P_Tessa_Cards_Validation_CardValidationContext_MainCard.htm)|
Основная карточка, для которой выполняется валидация.  
[MainCardMetadataBinder](P_Tessa_Cards_Validation_CardValidationContext_MainCardMetadataBinder.htm)|
Объект, выполняющий действия с основной карточкой, для которой выполняется
валидация.  
[MainCardType](P_Tessa_Cards_Validation_CardValidationContext_MainCardType.htm)|
Тип основной карточки, для которой выполняется валидация.  
[Session](P_Tessa_Cards_Validation_CardValidationContext_Session.htm)| Сессия
пользователя, в процессе работы которого выполняется валидация.  
[StoreMode](P_Tessa_Cards_Validation_CardValidationContext_StoreMode.htm)|
Способ сохранения проверяемого объекта - карточки, файла или задания.  
[TaskCard](P_Tessa_Cards_Validation_CardValidationContext_TaskCard.htm)|
Карточка задания, валидация которой выполняется, или null, если задание
завершается без данных карточки или валидация задания не выполняется.  
[TaskCardMetadataBinder](P_Tessa_Cards_Validation_CardValidationContext_TaskCardMetadataBinder.htm)|
Объект, выполняющий действия с карточкой задания, для которой выполняется
валидация, или null, если задание завершается без данных карточки или
валидация задания не выполняется.  
[TaskCardType](P_Tessa_Cards_Validation_CardValidationContext_TaskCardType.htm)|
Тип карточки задания, для которой выполняется валидация, или null, если
валидация задания не выполняется.  
[ValidationMode](P_Tessa_Cards_Validation_CardValidationContext_ValidationMode.htm)|
Способ выполнения валидации.  
##  __Методы
[BuildResult](M_Tessa_Cards_Validation_CardValidationContext_BuildResult.htm)|
Выполняет построение результата валидации карточки.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetCardValidator](M_Tessa_Cards_Validation_CardValidationContext_GetCardValidator.htm)|
Возвращает объект, выполняющий построение результата валидации для всей
карточки.  
[GetEntryFieldValidator](M_Tessa_Cards_Validation_CardValidationContext_GetEntryFieldValidator.htm)|
Возвращает объект, выполняющий построение результата валидации для заданного
поля строковой секции.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSectionValidator](M_Tessa_Cards_Validation_CardValidationContext_GetSectionValidator.htm)|
Возвращает объект, выполняющий построение результата валидации для строковой,
коллекционной или древовидной секции карточки.  
[GetTableFieldValidator](M_Tessa_Cards_Validation_CardValidationContext_GetTableFieldValidator.htm)|
Возвращает объект, выполняющий построение результата валидации для заданного
поля строки коллекционной или древовидной секции.  
[GetTableRowValidator](M_Tessa_Cards_Validation_CardValidationContext_GetTableRowValidator.htm)|
Возвращает объект, выполняющий построение результата валидации для строки
коллекционной или древовидной секции.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync](M_Tessa_Cards_Validation_CardValidationContext_InitializeAsync.htm)|
Выполняет асинхронную инициализацию объекта.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Seal](M_Tessa_Cards_Validation_CardValidationContext_Seal.htm)| Защищает
объект от изменений.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
