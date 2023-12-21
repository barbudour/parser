# CardSerializableObjectContext.Create - метод
Создаёт область операции, в которой заданный контекст будет являться текущим.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IScopeContextInstance<ICardSerializableObjectContext> Create(
    	ICardSerializableObjectContext context
    )
VB __Копировать
     Public Shared Function Create ( 
    	context As ICardSerializableObjectContext
    ) As IScopeContextInstance(Of ICardSerializableObjectContext)
C++ __Копировать
     public:
    static IScopeContextInstance<ICardSerializableObjectContext^>^ Create(
    	ICardSerializableObjectContext^ context
    )
F# __Копировать
     static member Create : 
            context : ICardSerializableObjectContext -> IScopeContextInstance<ICardSerializableObjectContext> 
#### Параметры
context
[ICardSerializableObjectContext](T_Tessa_Cards_ICardSerializableObjectContext.htm)
    Контекст, для которого создаётся область операции.
#### Возвращаемое значение
[IScopeContextInstance](T_Tessa_Platform_Scopes_IScopeContextInstance_1.htm)<[ICardSerializableObjectContext](T_Tessa_Cards_ICardSerializableObjectContext.htm)>  
Область операции, в которой заданный контекст будет являться текущим.
##  __См. также
#### Ссылки
[CardSerializableObjectContext -
](T_Tessa_Cards_CardSerializableObjectContext.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
