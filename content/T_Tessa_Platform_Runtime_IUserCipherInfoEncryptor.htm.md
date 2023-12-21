# IUserCipherInfoEncryptor - интерфейс
Объект, обеспечивающий шифрование объекта
[UserCipherInfoObject](T_Tessa_Platform_Runtime_UserCipherInfoObject.htm) с
настройками по шифрованию клиентских данных.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUserCipherInfoEncryptor
VB __Копировать
     Public Interface IUserCipherInfoEncryptor
C++ __Копировать
     public interface class IUserCipherInfoEncryptor
F# __Копировать
     type IUserCipherInfoEncryptor = interface end
##  __Методы
[DecryptAsync](M_Tessa_Platform_Runtime_IUserCipherInfoEncryptor_DecryptAsync.htm)|
Выполняет расшифровку указанного объекта для того, чтобы можно его можно было
использовать. Такой объект можно держать только в оперативной памяти и нельзя
сохранять в базу данных.  
---|---  
[EncryptAsync](M_Tessa_Platform_Runtime_IUserCipherInfoEncryptor_EncryptAsync.htm)|
Шифрует указанный объект для того, чтобы можно было хранить его в таком виде в
базе данных или других потенциально опасных местах.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
