# CardFileSource.UseSimpleNamingScheme - свойство
Признак того, что используется упрощённая схема именования папок, где для
карточек не создаются дополнительные подпапки. Значение true не рекомендуется,
если в системе возможны миллионы карточек с файлами, т.к. это приведёт к
миллионам подпапок внутри одной папки в файловой системе. Значение неактуально
для файлов в базе данных.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool UseSimpleNamingScheme { get; }
VB __Копировать
     Public ReadOnly Property UseSimpleNamingScheme As Boolean
    	Get
C++ __Копировать
     public:
    virtual property bool UseSimpleNamingScheme {
    	bool get () sealed;
    }
F# __Копировать
     abstract UseSimpleNamingScheme : bool with get
    override UseSimpleNamingScheme : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[ICardFileSource.UseSimpleNamingScheme](P_Tessa_Cards_ICardFileSource_UseSimpleNamingScheme.htm)  
##  __См. также
#### Ссылки
[CardFileSource - ](T_Tessa_Cards_CardFileSource.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
