# CardExtensionContext.DbScope - свойство
Объект, обеспечивающий взаимодействие с базой данных. Значение равно null на
клиенте и не равно null на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
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
[ICardExtensionContext.DbScope](P_Tessa_Cards_Extensions_ICardExtensionContext_DbScope.htm)  
##  __См. также
#### Ссылки
[CardExtensionContext - ](T_Tessa_Cards_Extensions_CardExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
