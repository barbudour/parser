# WebContext - класс
Контекст обработки на веб-сервере.
## __Definition
 **Пространство имён:** [Tessa.Web.Services](N_Tessa_Web_Services.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WebContext : IWebContext
VB __Копировать
     Public NotInheritable Class WebContext
    	Implements IWebContext
C++ __Копировать
     public ref class WebContext sealed : IWebContext
F# __Копировать
     [<SealedAttribute>]
    type WebContext = 
        class
            interface IWebContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WebContext
Implements
    [IWebContext](T_Tessa_Web_Services_IWebContext.htm)
##  __Конструкторы
[WebContext](M_Tessa_Web_Services_WebContext__ctor.htm)| Инициализирует новый
экземпляр класса WebContext  
---|---  
##  __Методы
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
[SetLocalizationService](M_Tessa_Web_Services_WebContext_SetLocalizationService.htm)|
Метод для установки
[ILocalizationService](T_Tessa_Localization_ILocalizationService.htm) в
контекст в качестве текущего сервиса локализации.  
[SetSessionToken](M_Tessa_Web_Services_WebContext_SetSessionToken.htm)|  Метод
для установки [ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm) в
контекст в качестве текущего токена, содержащего информацию о сессии.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetLocalizationService](M_Tessa_Web_Services_WebContext_TryGetLocalizationService.htm)|
Возвращает текущий сервис локализации, установленный через
[SetLocalizationService(ILocalizationService)](M_Tessa_Web_Services_IWebContext_SetLocalizationService.htm),
или null, если сервис локализации не установлен.  
[TryGetSessionToken](M_Tessa_Web_Services_WebContext_TryGetSessionToken.htm)|
Возвращает текущий токен, содержащий информацию о сессии, установленный через
[SetSessionToken(ISessionToken)](M_Tessa_Web_Services_IWebContext_SetSessionToken.htm),
или null, если токен не установлен.  
## __Методы расширения
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
[Tessa.Web.Services - пространство имён](N_Tessa_Web_Services.htm)
