# UserCipherInfoEncryptor - класс
Объект, обеспечивающий шифрование объекта
[UserCipherInfoObject](T_Tessa_Platform_Runtime_UserCipherInfoObject.htm) с
настройками по шифрованию клиентских данных.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class UserCipherInfoEncryptor : IUserCipherInfoEncryptor
VB __Копировать
     Public NotInheritable Class UserCipherInfoEncryptor
    	Implements IUserCipherInfoEncryptor
C++ __Копировать
     public ref class UserCipherInfoEncryptor sealed : IUserCipherInfoEncryptor
F# __Копировать
     [<SealedAttribute>]
    type UserCipherInfoEncryptor = 
        class
            interface IUserCipherInfoEncryptor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UserCipherInfoEncryptor
Implements
    [IUserCipherInfoEncryptor](T_Tessa_Platform_Runtime_IUserCipherInfoEncryptor.htm)
##  __Конструкторы
[UserCipherInfoEncryptor](M_Tessa_Platform_Runtime_UserCipherInfoEncryptor__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[DecryptAsync](M_Tessa_Platform_Runtime_UserCipherInfoEncryptor_DecryptAsync.htm)|
Выполняет расшифровку указанного объекта для того, чтобы можно его можно было
использовать. Такой объект можно держать только в оперативной памяти и нельзя
сохранять в базу данных.  
---|---  
[EncryptAsync](M_Tessa_Platform_Runtime_UserCipherInfoEncryptor_EncryptAsync.htm)|
Шифрует указанный объект для того, чтобы можно было хранить его в таком виде в
базе данных или других потенциально опасных местах.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
