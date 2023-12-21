# IContextPolicy<TContext> \- интерфейс
Политика, проверяющая условие для указанного контекста расширений.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IContextPolicy<in TContext> : IExtensionPolicy
    where TContext : class, IExtensionContext
VB __Копировать
     Public Interface IContextPolicy(Of In TContext As {Class, IExtensionContext})
    	Inherits IExtensionPolicy
C++ __Копировать
    generic<typename TContext>
    where TContext : ref class, IExtensionContext
    public interface class IContextPolicy : IExtensionPolicy
F# __Копировать
     type IContextPolicy<'TContext when 'TContext : not struct and IExtensionContext> = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
#### Параметры типа
TContext
    Ссылочный тип контекста расширений [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm).
##  __Методы
[IsAllowed](M_Tessa_Extensions_IContextPolicy_1_IsAllowed.htm)|  Признак того,
что политика выполняется для указанного контекста.  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
