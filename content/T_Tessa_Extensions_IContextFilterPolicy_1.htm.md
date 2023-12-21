# IContextFilterPolicy<TContext> \- интерфейс
Политика фильтрации расширений, использующая политику
[IContextPolicy<TContext>](T_Tessa_Extensions_IContextPolicy_1.htm) для того,
чтобы не выполнять методы расширений, для которых выполняется условие для
контекста TContext. Если зарегистрировано несколько политик, то должны
выполняться все из них.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IContextFilterPolicy<TContext> : IFilterPolicy, 
    	IExtensionPolicy
    where TContext : class, IExtensionContext
VB __Копировать
     Public Interface IContextFilterPolicy(Of TContext As {Class, IExtensionContext})
    	Inherits IFilterPolicy, IExtensionPolicy
C++ __Копировать
    generic<typename TContext>
    where TContext : ref class, IExtensionContext
    public interface class IContextFilterPolicy : IFilterPolicy, 
    	IExtensionPolicy
F# __Копировать
     type IContextFilterPolicy<'TContext when 'TContext : not struct and IExtensionContext> = 
        interface
            interface IFilterPolicy
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm), [IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm)
#### Параметры типа
TContext
    Ссылочный тип контекста расширений [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm).
##  __Методы
[FilterAsync](M_Tessa_Extensions_IFilterPolicy_FilterAsync.htm)|  Возвращает
признак того, что выполнение метода с заданным параметром разрешено для
экземпляра расширения.  
(Унаследован от [IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm))  
---|---  
[GetFilterContextAsync](M_Tessa_Extensions_IFilterPolicy_GetFilterContextAsync.htm)|
Возвращает контекст фильтрации, используемый для определение разрешений на
выполнение метода для экземпляров расширений.  
(Унаследован от [IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
