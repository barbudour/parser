# ViewCurrentUserParameters - класс
Представляет доступ к специальному параметру CurrentUserId
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ViewCurrentUserParameters : IViewCurrentUserParameters
VB __Копировать
     Public NotInheritable Class ViewCurrentUserParameters
    	Implements IViewCurrentUserParameters
C++ __Копировать
     public ref class ViewCurrentUserParameters sealed : IViewCurrentUserParameters
F# __Копировать
     [<SealedAttribute>]
    type ViewCurrentUserParameters = 
        class
            interface IViewCurrentUserParameters
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ViewCurrentUserParameters
Implements
    [IViewCurrentUserParameters](T_Tessa_Views_IViewCurrentUserParameters.htm)
##  __Конструкторы
[ViewCurrentUserParameters(ISession)](M_Tessa_Views_ViewCurrentUserParameters__ctor.htm)|
Initializes a new instance of the ViewCurrentUserParameters class.  
---|---  
[ViewCurrentUserParameters(ISession, Func<IViewParameterMetadata>,
Func<Boolean,
RequestParameterBuilder>)](M_Tessa_Views_ViewCurrentUserParameters__ctor_1.htm)|
Initializes a new instance of the ViewCurrentUserParameters class. Initializes
a new instance of the
[ViewSpecialParameters](T_Tessa_Views_ViewSpecialParameters.htm) class.  
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
[GetCurrentUserParameter(Boolean,
Boolean)](M_Tessa_Views_ViewCurrentUserParameters_GetCurrentUserParameter.htm)|
Создает и возвращает параметр текущий пользователь инициализированный
параметрами текущего пользователя  
[GetCurrentUserParameter(Guid, String, Boolean,
Boolean)](M_Tessa_Views_ViewCurrentUserParameters_GetCurrentUserParameter_1.htm)|
Создает и возвращает параметр текущий пользователь  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLocaleParameter](M_Tessa_Views_ViewCurrentUserParameters_GetLocaleParameter.htm)|
Создает и возвращает параметр Идентификатор культуры пользователя  
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
[ProvideCurrentUserIdParameter](M_Tessa_Views_ViewCurrentUserParameters_ProvideCurrentUserIdParameter.htm)|
Проставляет в список параметров значение текушего пользователя, если он там
отсутствует. В случае если в коллекции уже есть параметр с именем
[CurrentUserId](F_Tessa_Views_ViewSpecialParametersConst_CurrentUserId.htm) :
а) Пользователь не является администратором, осуществляем замену данного
параметра. б) Если пользователь является администратором, параметр остается
как есть.  
[ProvideLocaleParameter](M_Tessa_Views_ViewCurrentUserParameters_ProvideLocaleParameter.htm)|
Проставлеяет в список параметров идентификатор культуры. Если параметр уже
есть в списке он будет заменен  
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
