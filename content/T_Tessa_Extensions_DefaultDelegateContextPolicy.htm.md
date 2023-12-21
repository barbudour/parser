# DefaultDelegateContextPolicy - класс
Политика, проверяющая условие для указанного контекста расширений, которое
задаётся как делегат Func<IExtensionContext, bool>. Выполняется для любых
типов расширений, даже если не была явно зарегистрирована.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DefaultDelegateContextPolicy : DelegateContextPolicy<IExtensionContext>, 
    	IDefaultDelegateContextPolicy, IDelegateContextPolicy<IExtensionContext>, IContextPolicy<IExtensionContext>, 
    	IExtensionPolicy
VB __Копировать
     Public NotInheritable Class DefaultDelegateContextPolicy
    	Inherits DelegateContextPolicy(Of IExtensionContext)
    	Implements IDefaultDelegateContextPolicy, IDelegateContextPolicy(Of IExtensionContext), 
    	IContextPolicy(Of IExtensionContext), IExtensionPolicy
C++ __Копировать
     public ref class DefaultDelegateContextPolicy sealed : public DelegateContextPolicy<IExtensionContext^>, 
    	IDefaultDelegateContextPolicy, IDelegateContextPolicy<IExtensionContext^>, IContextPolicy<IExtensionContext^>, 
    	IExtensionPolicy
F# __Копировать
     [<SealedAttribute>]
    type DefaultDelegateContextPolicy = 
        class
            inherit DelegateContextPolicy<IExtensionContext>
            interface IDefaultDelegateContextPolicy
            interface IDelegateContextPolicy<IExtensionContext>
            interface IContextPolicy<IExtensionContext>
            interface IExtensionPolicy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DelegateContextPolicy](T_Tessa_Extensions_DelegateContextPolicy_1.htm)<[IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)> __ DefaultDelegateContextPolicy
Implements
    [IContextPolicy](T_Tessa_Extensions_IContextPolicy_1.htm)<[IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)>, [IDefaultDelegateContextPolicy](T_Tessa_Extensions_IDefaultDelegateContextPolicy.htm), [IDelegateContextPolicy](T_Tessa_Extensions_IDelegateContextPolicy_1.htm)<[IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)>, [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Конструкторы
[DefaultDelegateContextPolicy](M_Tessa_Extensions_DefaultDelegateContextPolicy__ctor.htm)|
Инициализирует новый экземпляр класса DefaultDelegateContextPolicy  
---|---  
##  __Свойства
[FilterPolicy](P_Tessa_Extensions_DefaultDelegateContextPolicy_FilterPolicy.htm)|
Политика фильтрации по умолчанию.  
---|---  
[IsAllowedFunc](P_Tessa_Extensions_DelegateContextPolicy_1_IsAllowedFunc.htm)|
Функция, получающая контекст (не равный null) и возвращающая признак того, что
контекст удовлетворяет политике. Значение не равно null.  
(Унаследован от
[DelegateContextPolicy<TContext>](T_Tessa_Extensions_DelegateContextPolicy_1.htm))  
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
[IsAllowed](M_Tessa_Extensions_DelegateContextPolicy_1_IsAllowed.htm)|
Признак того, что политика выполняется для указанного контекста.  
(Унаследован от
[DelegateContextPolicy<TContext>](T_Tessa_Extensions_DelegateContextPolicy_1.htm))  
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
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
