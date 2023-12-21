# ViewCardParameters - класс
Предоставляет параметры доступа к текущей карточке
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ViewCardParameters : IViewCardParameters
VB __Копировать
     Public NotInheritable Class ViewCardParameters
    	Implements IViewCardParameters
C++ __Копировать
     public ref class ViewCardParameters sealed : IViewCardParameters
F# __Копировать
     [<SealedAttribute>]
    type ViewCardParameters = 
        class
            interface IViewCardParameters
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ViewCardParameters
Implements
    [IViewCardParameters](T_Tessa_Views_IViewCardParameters.htm)
##  __Конструкторы
[ViewCardParameters()](M_Tessa_Views_ViewCardParameters__ctor.htm)|
Initializes a new instance of the ViewCardParameters class.  
---|---  
[ViewCardParameters(Func<IViewParameterMetadata>, Func<Boolean,
RequestParameterBuilder>)](M_Tessa_Views_ViewCardParameters__ctor_1.htm)|
Initializes a new instance of the ViewCardParameters class.  
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
[GetCardIdParameter](M_Tessa_Views_ViewCardParameters_GetCardIdParameter.htm)|
Создает и возвращает параметр Идентификатор текущей карточки  
[GetCardTypeIdParameter](M_Tessa_Views_ViewCardParameters_GetCardTypeIdParameter.htm)|
Создает и возвращает параметр идентификатор типа текущей карточки  
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
[ProvideCurrentCardIdParameter](M_Tessa_Views_ViewCardParameters_ProvideCurrentCardIdParameter.htm)|
Проставлеяет в список параметров идентификатор текущей карточки. Если параметр
уже есть в списке он будет заменен  
[ProvideCurrentCardTypeIdParameter](M_Tessa_Views_ViewCardParameters_ProvideCurrentCardTypeIdParameter.htm)|
Проставляет в список параметров идентификатор типа текущей карточки. Если
параметр уже есть в списке он будет заменен.  
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
