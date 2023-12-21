# CardNewContext - класс
Контекст операции по созданию карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardNewContext
VB __Копировать
     Public NotInheritable Class CardNewContext
C++ __Копировать
     public ref class CardNewContext sealed
F# __Копировать
     [<SealedAttribute>]
    type CardNewContext = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardNewContext
##  __Конструкторы
[CardNewContext](M_Tessa_Cards_ComponentModel_CardNewContext__ctor.htm)|
Создаёт экземпляр класса с указанием информации, необходимой для создания
карточки.  
---|---  
## __Свойства
[Card](P_Tessa_Cards_ComponentModel_CardNewContext_Card.htm)|  Создаваемая
карточка. Требуется инициализация посредством метода
[InitCard()](M_Tessa_Cards_ComponentModel_CardNewContext_InitCard.htm), в
противном случае возвращает null.  
---|---  
[CardMetadata](P_Tessa_Cards_ComponentModel_CardNewContext_CardMetadata.htm)|
Метаинформация по типам карточек.  
[CardTypeID](P_Tessa_Cards_ComponentModel_CardNewContext_CardTypeID.htm)|
Идентификатор типа создаваемой карточки.  
[Mode](P_Tessa_Cards_ComponentModel_CardNewContext_Mode.htm)|  Способ создания
карточки.  
[SectionRows](P_Tessa_Cards_ComponentModel_CardNewContext_SectionRows.htm)|
Пустые строки коллекционных или древовидных секций создаваемой карточки,
доступные по имени секции. Требуется инициализация посредством метода
[InitResponse(CardNewResponse)](M_Tessa_Cards_ComponentModel_CardNewContext_InitResponse.htm),
в противном случае возвращает null.  
[ValidationResult](P_Tessa_Cards_ComponentModel_CardNewContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Требуется инициализация
посредством метода
[InitResponse(CardNewResponse)](M_Tessa_Cards_ComponentModel_CardNewContext_InitResponse.htm),
в противном случае возвращает null.  
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
[InitCard](M_Tessa_Cards_ComponentModel_CardNewContext_InitCard.htm)|
Инициализирует объект создаваемой карточки
[Card](P_Tessa_Cards_ComponentModel_CardNewContext_Card.htm).  
[InitResponse](M_Tessa_Cards_ComponentModel_CardNewContext_InitResponse.htm)|
Инициализирует свойства
[SectionRows](P_Tessa_Cards_ComponentModel_CardNewContext_SectionRows.htm) и
[ValidationResult](P_Tessa_Cards_ComponentModel_CardNewContext_ValidationResult.htm)
для заданного объекта, содержащего ответа на запрос по созданию карточки.  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
