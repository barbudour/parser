# CardDeleteScopeContext.Create - метод
Создаёт область операции, в которой заданный контекст будет являться текущим.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IScopeContextInstance<ICardDeleteScopeContext> Create(
    	ICardDeleteScopeContext context
    )
VB __Копировать
     Public Shared Function Create ( 
    	context As ICardDeleteScopeContext
    ) As IScopeContextInstance(Of ICardDeleteScopeContext)
C++ __Копировать
     public:
    static IScopeContextInstance<ICardDeleteScopeContext^>^ Create(
    	ICardDeleteScopeContext^ context
    )
F# __Копировать
     static member Create : 
            context : ICardDeleteScopeContext -> IScopeContextInstance<ICardDeleteScopeContext> 
#### Параметры
context
[ICardDeleteScopeContext](T_Tessa_Cards_ComponentModel_ICardDeleteScopeContext.htm)
    Контекст, для которого создаётся область операции.
#### Возвращаемое значение
[IScopeContextInstance](T_Tessa_Platform_Scopes_IScopeContextInstance_1.htm)<[ICardDeleteScopeContext](T_Tessa_Cards_ComponentModel_ICardDeleteScopeContext.htm)>  
Область операции, в которой заданный контекст будет являться текущим.
##  __См. также
#### Ссылки
[CardDeleteScopeContext -
](T_Tessa_Cards_ComponentModel_CardDeleteScopeContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
