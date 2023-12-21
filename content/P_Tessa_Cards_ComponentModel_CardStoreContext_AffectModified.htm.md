# CardStoreContext.AffectModified - свойство
Признак того, что изменения влияют на изменение информации по тому, когда
произошло изменение карточки и какой пользователь его выполнил. Это поле
эффективно только в случае, если значение свойства
[AffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_AffectVersion.htm)
равно false.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool AffectModified { get; set; }
VB __Копировать
     Public Property AffectModified As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool AffectModified {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member AffectModified : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
