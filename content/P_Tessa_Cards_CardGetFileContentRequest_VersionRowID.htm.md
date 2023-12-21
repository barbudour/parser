# CardGetFileContentRequest.VersionRowID - свойство
Идентификатор версии файла, контент которого запрашивается, или null, если
запрашивается виртуальная версия файла, идентификатор которой задаётся другим
способом. По умолчанию значение равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? VersionRowID { get; set; }
VB __Копировать
     Public Property VersionRowID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> VersionRowID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member VersionRowID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __См. также
#### Ссылки
[CardGetFileContentRequest - ](T_Tessa_Cards_CardGetFileContentRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
