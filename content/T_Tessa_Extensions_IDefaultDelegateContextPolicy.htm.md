# IDefaultDelegateContextPolicy - интерфейс
Политика, проверяющая условие для указанного контекста расширений, которое
задаётся как делегат Func<IExtensionContext, bool>. Выполняется для любых
типов расширений, даже если не была явно зарегистрирована.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IDefaultDelegateContextPolicy : IDelegateContextPolicy<IExtensionContext>, 
    	IContextPolicy<IExtensionContext>, IExtensionPolicy
VB __Копировать
     Public Interface IDefaultDelegateContextPolicy
    	Inherits IDelegateContextPolicy(Of IExtensionContext), IContextPolicy(Of IExtensionContext), 
    	IExtensionPolicy
C++ __Копировать
     public interface class IDefaultDelegateContextPolicy : IDelegateContextPolicy<IExtensionContext^>, 
    	IContextPolicy<IExtensionContext^>, IExtensionPolicy
F# __Копировать
     type IDefaultDelegateContextPolicy = 
        interface
            interface IDelegateContextPolicy<IExtensionContext>
            interface IContextPolicy<IExtensionContext>
            interface IExtensionPolicy
        end
Implements
    [IContextPolicy](T_Tessa_Extensions_IContextPolicy_1.htm)<[IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)>, [IDelegateContextPolicy](T_Tessa_Extensions_IDelegateContextPolicy_1.htm)<[IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)>, [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Методы
[IsAllowed](M_Tessa_Extensions_IContextPolicy_1_IsAllowed.htm)|  Признак того,
что политика выполняется для указанного контекста.  
(Унаследован от
[IContextPolicy<TContext>](T_Tessa_Extensions_IContextPolicy_1.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
