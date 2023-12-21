# IScopeContextInstanceBase<TContext> \- интерфейс
Экземпляр области операции с контекстом, который относится как к текущей, так
и к родительской области.
## __Definition
 **Пространство имён:** [Tessa.Platform.Scopes](N_Tessa_Platform_Scopes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IScopeContextInstanceBase<out TContext>
VB __Копировать
     Public Interface IScopeContextInstanceBase(Of Out TContext)
C++ __Копировать
    generic<typename TContext>
    public interface class IScopeContextInstanceBase
F# __Копировать
     type IScopeContextInstanceBase<'TContext> = interface end
#### Параметры типа
TContext
    Тип контекста операции.
##  __Свойства
[Context](P_Tessa_Platform_Scopes_IScopeContextInstanceBase_1_Context.htm)|
Контекст, установленный внутри текущей операции.  
---|---  
[Parent](P_Tessa_Platform_Scopes_IScopeContextInstanceBase_1_Parent.htm)|
Информация по родительскому контексту или null, если родительский контекст
отсутствует.  
## __См. также
#### Ссылки
[Tessa.Platform.Scopes - пространство имён](N_Tessa_Platform_Scopes.htm)
