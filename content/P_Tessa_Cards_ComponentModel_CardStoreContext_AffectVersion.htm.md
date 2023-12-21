# CardStoreContext.AffectVersion - свойство
Признак того, что изменения влияют на проверку и инкремент версии карточки.
При инкременте версии также изменяется информация по тому, когда произошло
изменение карточки и какой пользователь его выполнил. Этот флаг менее
приоритетный, чем
[DoesNotAffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_DoesNotAffectVersion.htm).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool AffectVersion { get; set; }
VB __Копировать
     Public Property AffectVersion As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool AffectVersion {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member AffectVersion : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
