# CardHelper.SystemRestoreKey - поле
Ключ для логического значения с признаком необходимости восстановления
карточки, которое записывается в
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) запроса на удаление
удалённой карточки. Ключ является системным и его не следует использовать для
других целей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public const string SystemRestoreKey = ".restore"
VB __Копировать
     Public Const SystemRestoreKey As String = ".restore"
C++ __Копировать
     public:
    literal String^ SystemRestoreKey = ".restore"
F# __Копировать
     static val mutable SystemRestoreKey: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Для получения значения ключа в расширениях можно использовать метод
[GetRestoreMode(CardDeleteRequest)](M_Tessa_Cards_CardRequestExtensions_GetRestoreMode.htm).
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
