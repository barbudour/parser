# CardRepairExtensionContext - класс
Контекст расширений на исправление структуры карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardRepairExtensionContext : ICardRepairExtensionContext, 
    	ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
VB __Копировать
     Public NotInheritable Class CardRepairExtensionContext
    	Implements ICardRepairExtensionContext, ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
C++ __Копировать
     public ref class CardRepairExtensionContext sealed : ICardRepairExtensionContext, 
    	ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type CardRepairExtensionContext = 
        class
            interface ICardRepairExtensionContext
            interface ICardTypeExtensionContext
            interface IExtensionContext
            interface ITraceableExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardRepairExtensionContext
Implements
    [ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm), [ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm)
##  __Конструкторы
[CardRepairExtensionContext](M_Tessa_Cards_Extensions_CardRepairExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Cards_Extensions_CardRepairExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[Card](P_Tessa_Cards_Extensions_CardRepairExtensionContext_Card.htm)|
Карточка, для которой выполняется исправление структуры.  
[CardMetadata](P_Tessa_Cards_Extensions_CardRepairExtensionContext_CardMetadata.htm)|
Метаинформация по типам карточек.  
[CardType](P_Tessa_Cards_Extensions_CardRepairExtensionContext_CardType.htm)|
Тип карточки или null, если тип карточки неизвестен.  
[CardTypeName](P_Tessa_Cards_Extensions_CardRepairExtensionContext_CardTypeName.htm)|
Уникальное имя типа карточки или null, если тип карточки неизвестен. Имя может
не соответствовать действительному типу в метаинформации.  
[DefaultManager](P_Tessa_Cards_Extensions_CardRepairExtensionContext_DefaultManager.htm)|
Объект, управляющий исправлением структуры карточки без расширений.  
[EnableTracing](P_Tessa_Cards_Extensions_CardRepairExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
[ExtendedManager](P_Tessa_Cards_Extensions_CardRepairExtensionContext_ExtendedManager.htm)|
Объект, управляющий исправлением структуры карточки с расширениями.  
[Info](P_Tessa_Cards_Extensions_CardRepairExtensionContext_Info.htm)|
Дополнительная информация для расширений.  
[NewMode](P_Tessa_Cards_Extensions_CardRepairExtensionContext_NewMode.htm)|
Способ заполнения полей значениями по умолчанию при исправлении структуры.  
[NotifyFieldsUpdated](P_Tessa_Cards_Extensions_CardRepairExtensionContext_NotifyFieldsUpdated.htm)|
Признак того, что при исправлении структуры значения полей требуется изменить
с уведомлениями об изменениях.  
[ParentContext](P_Tessa_Cards_Extensions_CardRepairExtensionContext_ParentContext.htm)|
Контекст по исправлению родительской карточки или null, если текущая
исправляемая карточка не связана с родительской карточкой, т.е. не является
сателлитом.  
[RequestIsSuccessful](P_Tessa_Cards_Extensions_CardRepairExtensionContext_RequestIsSuccessful.htm)|
Признак того, что исправление структуры карточки выполнено успешно. Свойство
принимает актуальное значение только после того, как исправление структуры
было выполнено стандартными средствами.  
[ValidationResult](P_Tessa_Cards_Extensions_CardRepairExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[RepairAsync](M_Tessa_Cards_CardExtensions_RepairAsync.htm)|  Выполняет
исправление структуры заданной карточки на основании данных в контексте
расширений по исправлению карточки. Метод полезен для исправления карточек-
сателлитов, связанных с основной исправляемой карточкой. После исправления
любые сообщения будут записаны в результат валидации текущего контекста.
Возвращает признак того, что исправление выполнено успешно, т.е. без ошибок,
предотвращающих использование карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
