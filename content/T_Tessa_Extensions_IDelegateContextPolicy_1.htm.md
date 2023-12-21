# IDelegateContextPolicy<TContext> \- интерфейс
Политика, проверяющая условие для указанного контекста расширений, которое
задаётся как делегат Func<TContext, bool>.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IDelegateContextPolicy<in TContext> : IContextPolicy<TContext>, 
    	IExtensionPolicy
    where TContext : class, IExtensionContext
VB __Копировать
     Public Interface IDelegateContextPolicy(Of In TContext As {Class, IExtensionContext})
    	Inherits IContextPolicy(Of TContext), IExtensionPolicy
C++ __Копировать
    generic<typename TContext>
    where TContext : ref class, IExtensionContext
    public interface class IDelegateContextPolicy : IContextPolicy<TContext>, 
    	IExtensionPolicy
F# __Копировать
     type IDelegateContextPolicy<'TContext when 'TContext : not struct and IExtensionContext> = 
        interface
            interface IContextPolicy<'TContext>
            interface IExtensionPolicy
        end
Implements
    [IContextPolicy](T_Tessa_Extensions_IContextPolicy_1.htm)<TContext>, [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
#### Параметры типа
TContext
    Ссылочный тип контекста расширений [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm).
##  __Методы
[IsAllowed](M_Tessa_Extensions_IContextPolicy_1_IsAllowed.htm)|  Признак того,
что политика выполняется для указанного контекста.  
(Унаследован от
[IContextPolicy<TContext>](T_Tessa_Extensions_IContextPolicy_1.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
