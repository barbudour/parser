# ContextFilterPolicy<TContext, TPolicy> \- класс
Политика фильтрации расширений, использующая политику
[IContextPolicy<TContext>](T_Tessa_Extensions_IContextPolicy_1.htm) для того,
чтобы не выполнять методы расширений, для которых выполняется условие для
контекста TContext. Если зарегистрировано несколько политик, то должны
выполняться все из них.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ContextFilterPolicy<TContext, TPolicy> : IContextFilterPolicy<TContext>, 
    	IFilterPolicy, IExtensionPolicy
    where TContext : class, IExtensionContext
    where TPolicy : class, Object, IContextPolicy<TContext>
VB __Копировать
     Public NotInheritable Class ContextFilterPolicy(Of TContext As {Class, IExtensionContext}, TPolicy As {Class, Object, IContextPolicy(Of TContext)})
    	Implements IContextFilterPolicy(Of TContext), IFilterPolicy, 
    	IExtensionPolicy
C++ __Копировать
    generic<typename TContext, typename TPolicy>
    where TContext : ref class, IExtensionContext
    where TPolicy : ref class, Object, IContextPolicy<TContext>
    public ref class ContextFilterPolicy sealed : IContextFilterPolicy<TContext>, 
    	IFilterPolicy, IExtensionPolicy
F# __Копировать
     [<SealedAttribute>]
    type ContextFilterPolicy<'TContext, 'TPolicy when 'TContext : not struct and IExtensionContext when 'TPolicy : not struct and Object and IContextPolicy<'TContext>> = 
        class
            interface IContextFilterPolicy<'TContext>
            interface IFilterPolicy
            interface IExtensionPolicy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ContextFilterPolicy<TContext, TPolicy>
Implements
    [IContextFilterPolicy](T_Tessa_Extensions_IContextFilterPolicy_1.htm)<TContext>, [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm), [IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm)
#### Параметры типа
TContext
    Ссылочный тип контекста расширений [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm).
TPolicy
    Ссылочный тип проверяемой политики [IContextPolicy<TContext>](T_Tessa_Extensions_IContextPolicy_1.htm).
##  __Конструкторы
[ContextFilterPolicy<TContext,
TPolicy>](M_Tessa_Extensions_ContextFilterPolicy_2__ctor.htm)| Инициализирует
новый экземпляр класса ContextFilterPolicy<TContext, TPolicy>  
---|---  
##  __Свойства
[Instance](P_Tessa_Extensions_ContextFilterPolicy_2_Instance.htm)| Экземпляр
класса.  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[FilterAsync](M_Tessa_Extensions_ContextFilterPolicy_2_FilterAsync.htm)|
Возвращает признак того, что выполнение метода с заданным параметром разрешено
для экземпляра расширения.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetFilterContextAsync](M_Tessa_Extensions_ContextFilterPolicy_2_GetFilterContextAsync.htm)|
Возвращает контекст фильтрации, используемый для определение разрешений на
выполнение метода для экземпляров расширений.  
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
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
