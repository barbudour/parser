# DelegateContextPolicy<TContext>.IsAllowed - метод
Признак того, что политика выполняется для указанного контекста.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual bool IsAllowed(
    	IExtension extension,
    	TContext context
    )
VB __Копировать
     Public Overridable Function IsAllowed ( 
    	extension As IExtension,
    	context As TContext
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsAllowed(
    	IExtension^ extension, 
    	TContext context
    )
F# __Копировать
     abstract IsAllowed : 
            extension : IExtension * 
            context : 'TContext -> bool 
    override IsAllowed : 
            extension : IExtension * 
            context : 'TContext -> bool 
#### Параметры
extension [IExtension](T_Tessa_Extensions_IExtension.htm)
    Расширение, для которого выполняется проверка.
context [TContext](T_Tessa_Extensions_DelegateContextPolicy_1.htm)
    Проверяемый контекст расширений.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если политика выполняется для указанного контекста; false в противном
случае.
#### Реализации
[IContextPolicy<TContext>.IsAllowed(IExtension,
TContext)](M_Tessa_Extensions_IContextPolicy_1_IsAllowed.htm)  
##  __См. также
#### Ссылки
[DelegateContextPolicy<TContext> \-
](T_Tessa_Extensions_DelegateContextPolicy_1.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
