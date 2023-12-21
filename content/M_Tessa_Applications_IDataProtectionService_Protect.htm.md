# IDataProtectionService.Protect - метод
Осуществляет шифрование данных data
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    byte[] Protect(
    	[CanBeNullAttribute] byte[] data
    )
VB __Копировать
    <CanBeNullAttribute>
    Function Protect ( 
    	<CanBeNullAttribute> data As Byte()
    ) As Byte()
C++ __Копировать
    [CanBeNullAttribute]
    array<unsigned char>^ Protect(
    	[CanBeNullAttribute] array<unsigned char>^ data
    )
F# __Копировать
     [<CanBeNullAttribute>]
    abstract Protect : 
            [<CanBeNullAttribute>] data : byte[] -> byte[] 
#### Параметры
data [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
     Шифруемые данные 
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Массив с зашифрованными данными или null
## __См. также
#### Ссылки
[IDataProtectionService - ](T_Tessa_Applications_IDataProtectionService.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
