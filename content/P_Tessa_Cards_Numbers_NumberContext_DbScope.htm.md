# NumberContext.DbScope - свойство
Объект, предоставляющий доступ к базе данных, или null, если выполнение
происходит без доступа к базе данных, например, со стороны клиента.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IDbScope DbScope { get; }
VB __Копировать
     Public ReadOnly Property DbScope As IDbScope
    	Get
C++ __Копировать
     public:
    virtual property IDbScope^ DbScope {
    	IDbScope^ get () sealed;
    }
F# __Копировать
     abstract DbScope : IDbScope with get
    override DbScope : IDbScope with get
#### Значение свойства
[IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
#### Реализации
[INumberDependencies.DbScope](P_Tessa_Cards_Numbers_INumberDependencies_DbScope.htm)  
##  __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
