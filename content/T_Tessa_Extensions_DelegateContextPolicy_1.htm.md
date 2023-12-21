# DelegateContextPolicy<TContext> \- класс
Политика, проверяющая условие для указанного контекста расширений, которое
задаётся как делегат Func<TContext, bool>.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class DelegateContextPolicy<TContext> : IDelegateContextPolicy<TContext>, 
    	IContextPolicy<TContext>, IExtensionPolicy
    where TContext : class, IExtensionContext
VB __Копировать
     Public Class DelegateContextPolicy(Of TContext As {Class, IExtensionContext})
    	Implements IDelegateContextPolicy(Of TContext), IContextPolicy(Of TContext), 
    	IExtensionPolicy
C++ __Копировать
    generic<typename TContext>
    where TContext : ref class, IExtensionContext
    public ref class DelegateContextPolicy : IDelegateContextPolicy<TContext>, 
    	IContextPolicy<TContext>, IExtensionPolicy
F# __Копировать
     type DelegateContextPolicy<'TContext when 'TContext : not struct and IExtensionContext> = 
        class
            interface IDelegateContextPolicy<'TContext>
            interface IContextPolicy<'TContext>
            interface IExtensionPolicy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DelegateContextPolicy<TContext>
Derived
[Tessa.Extensions.DefaultDelegateContextPolicy](T_Tessa_Extensions_DefaultDelegateContextPolicy.htm)
Implements
    [IContextPolicy](T_Tessa_Extensions_IContextPolicy_1.htm)<TContext>, [IDelegateContextPolicy](T_Tessa_Extensions_IDelegateContextPolicy_1.htm)<TContext>, [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
#### Параметры типа
TContext
    Ссылочный тип контекста расширений [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm).
##  __Заметки
Наследники класса могут ограничить тип контекста TContext и переопределить
функцию [IsAllowed(IExtension,
TContext)](M_Tessa_Extensions_DelegateContextPolicy_1_IsAllowed.htm) для
проверки дополнительных условий.
## __Конструкторы
[DelegateContextPolicy<TContext>](M_Tessa_Extensions_DelegateContextPolicy_1__ctor.htm)|
Создаёт экземпляр класса с указанием делегата, проверяющего то, что контекст
удовлетворяет политике.  
---|---  
## __Свойства
[IsAllowedFunc](P_Tessa_Extensions_DelegateContextPolicy_1_IsAllowedFunc.htm)|
Функция, получающая контекст (не равный null) и возвращающая признак того, что
контекст удовлетворяет политике. Значение не равно null.  
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
