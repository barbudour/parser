# CurrentUserDataProtectionService.Unprotect - метод
Осуществляет расшифрование данных data
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public byte[] Unprotect(
    	byte[] data
    )
VB __Копировать
     Public Function Unprotect ( 
    	data As Byte()
    ) As Byte()
C++ __Копировать
     public:
    virtual array<unsigned char>^ Unprotect(
    	array<unsigned char>^ data
    ) sealed
F# __Копировать
     abstract Unprotect : 
            data : byte[] -> byte[] 
    override Unprotect : 
            data : byte[] -> byte[] 
#### Параметры
data [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
     Данные для расшифорвки 
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Расшифрованные данные
#### Реализации
[IDataProtectionService.Unprotect(Byte[])](M_Tessa_Applications_IDataProtectionService_Unprotect.htm)  
##  __См. также
#### Ссылки
[CurrentUserDataProtectionService -
](T_Tessa_Applications_CurrentUserDataProtectionService.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
