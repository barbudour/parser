# ViewSpecialParameters - класс
Класс предназначенный для проставления специальных параметров используемых в
представлениях На текущий момент отрабатываются параметры CurrentUserID -
текущий пользователь PageOffset - смещение от начала списка PageLimit -
количество элементов на странице CardId - идентификатор текущей карточки
CardTypeId - идентификатор типа текущей карточки Locale - идентификатор локали
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ViewSpecialParameters : IViewSpecialParameters, 
    	IViewPagingParameters, IViewCardParameters, IViewCurrentUserParameters
VB __Копировать
     Public Class ViewSpecialParameters
    	Implements IViewSpecialParameters, IViewPagingParameters, IViewCardParameters, IViewCurrentUserParameters
C++ __Копировать
     public ref class ViewSpecialParameters : IViewSpecialParameters, 
    	IViewPagingParameters, IViewCardParameters, IViewCurrentUserParameters
F# __Копировать
     type ViewSpecialParameters = 
        class
            interface IViewSpecialParameters
            interface IViewPagingParameters
            interface IViewCardParameters
            interface IViewCurrentUserParameters
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ViewSpecialParameters
Implements
    [IViewCardParameters](T_Tessa_Views_IViewCardParameters.htm), [IViewCurrentUserParameters](T_Tessa_Views_IViewCurrentUserParameters.htm), [IViewPagingParameters](T_Tessa_Views_IViewPagingParameters.htm), [IViewSpecialParameters](T_Tessa_Views_IViewSpecialParameters.htm)
##  __Конструкторы
[ViewSpecialParameters](M_Tessa_Views_ViewSpecialParameters__ctor.htm)|
Initializes a new instance of the ViewSpecialParameters class.  
---|---  
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
[GetCardIdParameter](M_Tessa_Views_ViewSpecialParameters_GetCardIdParameter.htm)|
Создает и возвращает параметр Идентификатор текущей карточки  
[GetCardTypeIdParameter](M_Tessa_Views_ViewSpecialParameters_GetCardTypeIdParameter.htm)|
Создает и возвращает параметр идентификатор типа текущей карточки  
[GetCurrentUserParameter(Boolean,
Boolean)](M_Tessa_Views_ViewSpecialParameters_GetCurrentUserParameter.htm)|
Создает и возвращает параметр текущий пользователь инициализированный
параметрами текущего пользователя  
[GetCurrentUserParameter(Guid, String, Boolean,
Boolean)](M_Tessa_Views_ViewSpecialParameters_GetCurrentUserParameter_1.htm)|
Создает и возвращает параметр текущий пользователь  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLocaleParameter](M_Tessa_Views_ViewSpecialParameters_GetLocaleParameter.htm)|
Создает и возвращает параметр Идентификатор культуры пользователя  
[GetPageLimitParameter](M_Tessa_Views_ViewSpecialParameters_GetPageLimitParameter.htm)|
Создает и возвращает параметр пейджинга - количество отображаемых данных  
[GetPageOffsetParameter](M_Tessa_Views_ViewSpecialParameters_GetPageOffsetParameter.htm)|
Создает и возвращает параметр пейджинга - смешение внутри списка  
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
[ProvideCurrentCardIdParameter](M_Tessa_Views_ViewSpecialParameters_ProvideCurrentCardIdParameter.htm)|
Проставлеяет в список параметров идентификатор текущей карточки. Если параметр
уже есть в списке он будет заменен  
[ProvideCurrentCardTypeIdParameter](M_Tessa_Views_ViewSpecialParameters_ProvideCurrentCardTypeIdParameter.htm)|
Проставляет в список параметров идентификатор типа текущей карточки. Если
параметр уже есть в списке он будет заменен.  
[ProvideCurrentUserIdParameter](M_Tessa_Views_ViewSpecialParameters_ProvideCurrentUserIdParameter.htm)|
Проставляет в список параметров значение текушего пользователя, если он там
отсутствует  
[ProvideLocaleParameter](M_Tessa_Views_ViewSpecialParameters_ProvideLocaleParameter.htm)|
Проставлеяет в список параметров идентификатор культуры. Если параметр уже
есть в списке он будет заменен  
[ProvidePageLimitParameter](M_Tessa_Views_ViewSpecialParameters_ProvidePageLimitParameter.htm)|
Проставляет в список параметров значение для параметра PageLimit  
[ProvidePageOffsetParameter](M_Tessa_Views_ViewSpecialParameters_ProvidePageOffsetParameter.htm)|
Проставляет в список параметров значение для параметра PageOffset  
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
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
