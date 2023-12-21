# CalendarNewExtension - класс
Автоматически проставляем дату и время для вновь добавленных строк в таблицу
исключений. Это нужно для удобства.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.BusinessCalendar](N_Tessa_Extensions_Default_Server_BusinessCalendar.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CalendarNewExtension : CardNewExtension
VB __Копировать
     Public NotInheritable Class CalendarNewExtension
    	Inherits CardNewExtension
C++ __Копировать
     public ref class CalendarNewExtension sealed : public CardNewExtension
F# __Копировать
     [<SealedAttribute>]
    type CalendarNewExtension = 
        class
            inherit CardNewExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardNewExtension](T_Tessa_Cards_Extensions_CardNewExtension.htm) __ CalendarNewExtension
##  __Конструкторы
[CalendarNewExtension](M_Tessa_Extensions_Default_Server_BusinessCalendar_CalendarNewExtension__ctor.htm)|
Инициализирует новый экземпляр класса CalendarNewExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Extensions_Default_Server_BusinessCalendar_CalendarNewExtension_AfterRequest.htm)|  
(Переопределяет
[CardNewExtension.AfterRequest(ICardNewExtensionContext)](M_Tessa_Cards_Extensions_CardNewExtension_AfterRequest.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardNewExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после создания
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardNewExtension](T_Tessa_Cards_Extensions_CardNewExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_CardNewExtension_BeforeRequest.htm)|
Действие, выполняемое перед созданием структуры карточки стандартными
средствами. Может установить ответ на запрос для того, чтобы создание
структуры карточки стандартными средствами не выполнялось.  
(Унаследован от
[CardNewExtension](T_Tessa_Cards_Extensions_CardNewExtension.htm))  
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
[Tessa.Extensions.Default.Server.BusinessCalendar - пространство
имён](N_Tessa_Extensions_Default_Server_BusinessCalendar.htm)
