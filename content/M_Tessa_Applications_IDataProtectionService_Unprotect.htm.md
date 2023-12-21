# IDataProtectionService.Unprotect - метод
Осуществляет расшифрование данных data
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    byte[] Unprotect(
    	[CanBeNullAttribute] byte[] data
    )
VB __Копировать
    <CanBeNullAttribute>
    Function Unprotect ( 
    	<CanBeNullAttribute> data As Byte()
    ) As Byte()
C++ __Копировать
    [CanBeNullAttribute]
    array<unsigned char>^ Unprotect(
    	[CanBeNullAttribute] array<unsigned char>^ data
    )
F# __Копировать
     [<CanBeNullAttribute>]
    abstract Unprotect : 
            [<CanBeNullAttribute>] data : byte[] -> byte[] 
#### Параметры
data [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
     Данные для расшифорвки 
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Расшифрованные данные или null
## __См. также
#### Ссылки
[IDataProtectionService - ](T_Tessa_Applications_IDataProtectionService.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
