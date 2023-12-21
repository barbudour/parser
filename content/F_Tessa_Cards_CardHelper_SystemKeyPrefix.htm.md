# CardHelper.SystemKeyPrefix - поле
Префикс системных свойств, располагающихся в произвольном месте в хранилище
объекта [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm).
Такие свойства не должны как-либо учитываться или изменяться пользовательским
кодом.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public const string SystemKeyPrefix = "."
VB __Копировать
     Public Const SystemKeyPrefix As String = "."
C++ __Копировать
     public:
    literal String^ SystemKeyPrefix = "."
F# __Копировать
     static val mutable SystemKeyPrefix: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Проверить, является ли ключ системным, можно посредством метода
[IsSystemKey(String)](M_Tessa_Cards_CardHelper_IsSystemKey.htm).
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
