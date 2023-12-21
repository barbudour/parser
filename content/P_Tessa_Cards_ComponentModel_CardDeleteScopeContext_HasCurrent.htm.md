# CardDeleteScopeContext.HasCurrent - свойство
Признак того, что текущий код выполняется внутри операции с контекстом
[ICardDeleteScopeContext](T_Tessa_Cards_ComponentModel_ICardDeleteScopeContext.htm),
а свойство
[Current](P_Tessa_Cards_ComponentModel_CardDeleteScopeContext_Current.htm)
ссылается на действительный контекст.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasCurrent { get; }
VB __Копировать
     Public Shared ReadOnly Property HasCurrent As Boolean
    	Get
C++ __Копировать
     public:
    static property bool HasCurrent {
    	bool get ();
    }
F# __Копировать
     static member HasCurrent : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Если текущее свойство возвращает false, то свойство
[Current](P_Tessa_Cards_ComponentModel_CardDeleteScopeContext_Current.htm)
возвращает ссылку на пустой контекст.
## __См. также
#### Ссылки
[CardDeleteScopeContext -
](T_Tessa_Cards_ComponentModel_CardDeleteScopeContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
