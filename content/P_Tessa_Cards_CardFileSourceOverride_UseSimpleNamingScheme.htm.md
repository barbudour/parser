# CardFileSourceOverride.UseSimpleNamingScheme - свойство
Признак того, что используется упрощённая схема именования папок, где для
карточек не создаются дополнительные подпапки. Значение true не рекомендуется,
если в системе возможны миллионы карточек с файлами, т.к. это приведёт к
миллионам подпапок внутри одной папки в файловой системе. Значение неактуально
для файлов в базе данных.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool? UseSimpleNamingScheme { get; set; }
VB __Копировать
     Public Property UseSimpleNamingScheme As Boolean?
    	Get
    	Set
C++ __Копировать
     public:
    virtual property Nullable<bool> UseSimpleNamingScheme {
    	Nullable<bool> get () sealed;
    	void set (Nullable<bool> value) sealed;
    }
F# __Копировать
     abstract UseSimpleNamingScheme : Nullable<bool> with get, set
    override UseSimpleNamingScheme : Nullable<bool> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
#### Реализации
[ICardFileSourceOverride.UseSimpleNamingScheme](P_Tessa_Cards_ICardFileSourceOverride_UseSimpleNamingScheme.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardFileSourceOverride - ](T_Tessa_Cards_CardFileSourceOverride.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
