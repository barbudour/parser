# IScopeContext<TContext> \- интерфейс
Область операции с контекстом.
## __Definition
 **Пространство имён:** [Tessa.Platform.Scopes](N_Tessa_Platform_Scopes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IScopeContext<TContext>
VB __Копировать
     Public Interface IScopeContext(Of TContext)
C++ __Копировать
    generic<typename TContext>
    public interface class IScopeContext
F# __Копировать
     type IScopeContext<'TContext> = interface end
#### Параметры типа
TContext
    Тип контекста операции.
##  __Свойства
[Context](P_Tessa_Platform_Scopes_IScopeContext_1_Context.htm)| Контекст,
установленный внутри текущей операции.  
---|---  
[Current](P_Tessa_Platform_Scopes_IScopeContext_1_Current.htm)|  Объект,
содержащий текущий контекст, или null, если текущий контекст отсутствует.  
[HasContext](P_Tessa_Platform_Scopes_IScopeContext_1_HasContext.htm)| Признак
того, что код исполняется внутри области операции, для которой определён
контекст.  
[Parent](P_Tessa_Platform_Scopes_IScopeContext_1_Parent.htm)|  Объект,
содержащий родительский контекст, или null, если текущий или родительский
контексты отсутствуют.  
## __Методы
[Create](M_Tessa_Platform_Scopes_IScopeContext_1_Create.htm)| Создаёт
экземпляр области операции, в пределах которой будет установлен заданный
контекст.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Scopes - пространство имён](N_Tessa_Platform_Scopes.htm)
