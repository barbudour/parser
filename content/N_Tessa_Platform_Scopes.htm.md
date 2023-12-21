# Tessa.Platform.Scopes - пространство имён
Вспомогательные классы для операций, которые выполняются в некотором
контексте. Контекст передаётся через стек вызовов.
##  __Классы
[InheritableRetainingScope<T>](T_Tessa_Platform_Scopes_InheritableRetainingScope_1.htm)|
Класс, позволяющий создавать наследуемые области видимости для объекта
заданного типа, которые могут "удерживаться" посредством области
[ScopeHolderContext](T_Tessa_Platform_Scopes_ScopeHolderContext.htm). Также
область видимости существует в контексте текущего контекста вызова
ExecutionContext, т.е. он "пробрасывается" при выполнении асинхронных действий
async/await. Наследуемость определяется тем, что во вложенных областях
видимости возвращается тот же объект, что был создан для внешней области
видимости.  
---|---  
[InheritableScope<T>](T_Tessa_Platform_Scopes_InheritableScope_1.htm)|  Класс,
позволяющий создавать наследуемые области видимости для объекта заданного
типа. Область видимости существует в контексте текущего контекста вызова
ExecutionContext, т.е. он "пробрасывается" при выполнении асинхронных действий
async/await. Наследуемость определяется тем, что во вложенных областях
видимости возвращается тот же объект, что был создан для внешней области
видимости.  
[ScopeContext<TContext>](T_Tessa_Platform_Scopes_ScopeContext_1.htm)|  Область
операции с контекстом.  
[ScopeHolderContext](T_Tessa_Platform_Scopes_ScopeHolderContext.htm)|
Контекст объекта, выполняющего удержание наследуемых контекстов. Например,
удержание автоматически происходит при выполнении расширений
[IExtensionExecutor<TExtension>](T_Tessa_Extensions_IExtensionExecutor_1.htm),
а также "между" цепочками расширений в API карточек.  
[ScopeRetainingContext<TContext>](T_Tessa_Platform_Scopes_ScopeRetainingContext_1.htm)|
Область операции с контекстом.  
## __Интерфейсы
[IInheritableScopeInstance<T>](T_Tessa_Platform_Scopes_IInheritableScopeInstance_1.htm)|
Экземпляр для наследуемой области видимости объекта заданного типа. Область
видимости существует в контексте текущего потока. Наследуемость определяется
тем, что во вложенных областях видимости возвращается тот же объект, что был
создан для внешней области видимости.  
---|---  
[IScopeContext<TContext>](T_Tessa_Platform_Scopes_IScopeContext_1.htm)|
Область операции с контекстом.  
[IScopeContextInstance<TContext>](T_Tessa_Platform_Scopes_IScopeContextInstance_1.htm)|
Экземпляр области операции с контекстом. Вызов
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) завершает операцию, причём текущей назначается предыдущая
операция.  
[IScopeContextInstanceBase<TContext>](T_Tessa_Platform_Scopes_IScopeContextInstanceBase_1.htm)|
Экземпляр области операции с контекстом, который относится как к текущей, так
и к родительской области.  
[IScopeHolderContext](T_Tessa_Platform_Scopes_IScopeHolderContext.htm)|
Контекст объекта, выполняющего удержание наследуемых контекстов. Например,
удержание автоматически происходит при выполнении расширений
[IExtensionExecutor<TExtension>](T_Tessa_Extensions_IExtensionExecutor_1.htm),
а также "между" цепочками расширений в API карточек.
