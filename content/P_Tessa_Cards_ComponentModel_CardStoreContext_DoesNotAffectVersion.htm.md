# CardStoreContext.DoesNotAffectVersion - свойство
Признак того, что изменение карточки не приведёт к проверке и к увеличению
номера версии, даже если присутствуют изменяемые значения в основной карточке
или её файлах. При первом сохранении карточки версия всё равно увеличивается
до 1. Этот флаг более приоритетный, чем
[AffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_AffectVersion.htm).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool DoesNotAffectVersion { get; set; }
VB __Копировать
     Public Property DoesNotAffectVersion As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool DoesNotAffectVersion {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member DoesNotAffectVersion : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
