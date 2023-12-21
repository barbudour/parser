# CardFileRequestBase.FileID - свойство
Идентификатор файла, информация по которому запрашивается, или null, если
информация запрашивается по виртуальному файлу, идентификатор которого
задаётся другим способом. По умолчанию значение равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? FileID { get; set; }
VB __Копировать
     Public Property FileID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> FileID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member FileID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __См. также
#### Ссылки
[CardFileRequestBase - ](T_Tessa_Cards_CardFileRequestBase.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
