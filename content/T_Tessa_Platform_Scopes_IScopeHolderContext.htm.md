# IScopeHolderContext - интерфейс
Контекст объекта, выполняющего удержание наследуемых контекстов. Например,
удержание автоматически происходит при выполнении расширений
[IExtensionExecutor<TExtension>](T_Tessa_Extensions_IExtensionExecutor_1.htm),
а также "между" цепочками расширений в API карточек.
## __Definition
 **Пространство имён:** [Tessa.Platform.Scopes](N_Tessa_Platform_Scopes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IScopeHolderContext
VB __Копировать
     Public Interface IScopeHolderContext
C++ __Копировать
     public interface class IScopeHolderContext
F# __Копировать
     type IScopeHolderContext = interface end
##  __Методы
[Set](M_Tessa_Platform_Scopes_IScopeHolderContext_Set.htm)|  Устанавливает
объект, удерживаемый в контексте для заданного типа, или null, если объект
удаляется.  
---|---  
[TryGet](M_Tessa_Platform_Scopes_IScopeHolderContext_TryGet.htm)|  Возвращает
объект, удерживаемый в контексте для заданного типа, или null, если объект
отсутствует.  
## __См. также
#### Ссылки
[Tessa.Platform.Scopes - пространство имён](N_Tessa_Platform_Scopes.htm)
