# CardActionTextDescriptionBuilder - класс
Объект, выполняющий построение текстового описания действия с карточкой в
простом текстовом формате.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardActionTextDescriptionBuilder : ICardActionDescriptionBuilder
VB __Копировать
     Public NotInheritable Class CardActionTextDescriptionBuilder
    	Implements ICardActionDescriptionBuilder
C++ __Копировать
     public ref class CardActionTextDescriptionBuilder sealed : ICardActionDescriptionBuilder
F# __Копировать
     [<SealedAttribute>]
    type CardActionTextDescriptionBuilder = 
        class
            interface ICardActionDescriptionBuilder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardActionTextDescriptionBuilder
Implements
    [ICardActionDescriptionBuilder](T_Tessa_Cards_ComponentModel_ICardActionDescriptionBuilder.htm)
##  __Конструкторы
[CardActionTextDescriptionBuilder](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder__ctor.htm)|
Создаёт экземпляр класса с указанием метаинформации по типам карточек.  
---|---  
## __Методы
[AppendCardAsync](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendCardAsync.htm)|
Добавляет описание изменений, произошедших в заданной карточке. Актуально
только для действий [Tessa.Cards.CardActionType.Create] и
[Tessa.Cards.CardActionType.Modify].  
---|---  
[AppendHeaderAsync(StringBuilder, CardDeleteRequest,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendHeaderAsync.htm)|
Добавляет описание заголовка для запроса на удаление карточки.  
[AppendHeaderAsync(StringBuilder, CardGetFileContentRequest,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendHeaderAsync_1.htm)|
Добавляет описание заголовка для запроса на загрузку контента файла.  
[AppendHeaderAsync(StringBuilder, CardGetRequest,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendHeaderAsync_2.htm)|
Добавляет описание заголовка для запроса на загрузку карточки.  
[AppendHeaderAsync(StringBuilder, CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendHeaderAsync_3.htm)|
Добавляет описание заголовка для запроса на создание или изменение карточки.  
[AppendHeaderAsync(StringBuilder, CardTypeStoreRequest,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendHeaderAsync_4.htm)|
Добавляет описание заголовка для запроса на сохранение типов карточек.  
[AppendHeaderAsync(StringBuilder, LocalizationStoreRequest,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendHeaderAsync_5.htm)|
Добавляет описание заголовка для запроса на сохранение библиотеки локализации.  
[AppendHeaderAsync(StringBuilder, SchemeStoreRequest,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendHeaderAsync_6.htm)|
Добавляет описание заголовка для запроса на сохранение схемы данных.  
[AppendHeaderAsync(StringBuilder, ViewStoreRequest,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendHeaderAsync_7.htm)|
Добавляет описание заголовка для запроса на сохранение представлений.  
[AppendHeaderAsync(StringBuilder, WorkplaceStoreRequest,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendHeaderAsync_8.htm)|
Добавляет описание заголовка для запроса на сохранение рабочих мест.  
[AppendLoginAsync](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendLoginAsync.htm)|
Добавляет текст описания для записи в истории, которая относится к
выполненному входу в систему.  
[AppendLoginFailedAsync](M_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendLoginFailedAsync.htm)|
Добавляет текст описания для записи в истории, которая относится к неудачной
попытке входа в систему.  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
