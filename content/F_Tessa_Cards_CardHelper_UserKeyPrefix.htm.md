# CardHelper.UserKeyPrefix - поле
Префикс пользовательских свойств, располагающихся в произвольном месте в
хранилище объекта
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public const string UserKeyPrefix = "__"
VB __Копировать
     Public Const UserKeyPrefix As String = "__"
C++ __Копировать
     public:
    literal String^ UserKeyPrefix = "__"
F# __Копировать
     static val mutable UserKeyPrefix: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Пользовательские свойства могут быть удалены из хранилища объекта
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm) вызовом
метода
[RemoveUserInfo()](M_Tessa_Cards_CardInfoStorageObject_RemoveUserInfo.htm).
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
